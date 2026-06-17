import { EventEmitter } from "./eventEmitter.js";
import { packageGenerator, consumeGeneratorWithTimeout } from "./generator.js";
import { memoize } from "./memoize.js";
import { PriorityQueue } from "./priorityQueue.js";
import { asyncFilter } from "./asyncFilter.js";
import { createAsyncStream } from "./asyncStream.js";
import { ApiService, AuthProxy } from "./authProxy.js";
import { withLogging } from "./logger.js";

async function runSimulation() {
    console.log("=== STARTING WAREHOUSE SIMULATION ===");

    const warehouseEvents = new EventEmitter();
    warehouseEvents.subscribe("package_arrived", (pkg) => {
        console.log(`Notification: Package #${pkg.id} (${pkg.type}) arrived at warehouse.`);
    });

    const calculation = (weight, distance) => {
        let base = weight * 2.5 + distance * 1.2;
        return +(base.toFixed(2));
    };
    const loggedCalculation = withLogging("INFO", calculation);
    const memoizedCostCalc = memoize(loggedCalculation, { maxSize: 3, policy: "LRU" });

    const outboundQueue = new PriorityQueue();

    console.log("\n--- Processing Incoming Stream ---");
    await consumeGeneratorWithTimeout(packageGenerator, 1.5, (pkg) => {
        warehouseEvents.emit("package_arrived", pkg);
        let priority = 1;
        if (pkg.type === "VIP") priority = 10;
        if (pkg.type === "Express") priority = 5;
        outboundQueue.enqueue(pkg, priority);
    });

    console.log("\n--- Testing Memoized Cost Calculation ---");
    console.log("First calc (10kg, 100km):", memoizedCostCalc(10, 100));
    console.log("Second calc (10kg, 100km) [Should cache & not log]:", memoizedCostCalc(10, 100));
    console.log("Third calc (5kg, 50km):", memoizedCostCalc(5, 50));

    console.log("\n--- Queue Dispatching (Highest Priority First) ---");
    let nextToDispatch = outboundQueue.dequeue(true, true);
    while (nextToDispatch) {
        console.log(`Dispatching Package #${nextToDispatch.id} | Type: ${nextToDispatch.type}`);
        nextToDispatch = outboundQueue.dequeue(true, true);
    }

    console.log("\n--- Async Filter with Cancellation ---");
    const testPackages = [
        { id: 101, weight: 5 },
        { id: 102, weight: 45 },
        { id: 103, weight: 12 }
    ];
    const controller = new AbortController();
    try {
        const heavyPackages = await asyncFilter(testPackages, async (p) => {
            return p.weight > 10;
        }, controller.signal);
        console.log("Heavy packages found:", heavyPackages);
    } catch (err) {
        console.log("Filter error:", err.message);
    }

    console.log("\n--- Streaming Mock Large Archive Logs ---");
    const heavyLogs = [
        "Log Entry: Item 401 scanned",
        "Log Entry: Item 402 sorted",
        "Log Entry: Item 403 loaded"
    ];
    const stream = createAsyncStream(heavyLogs);
    for await (const chunk of stream) {
        console.log(`Stream Chunk Processed: ${chunk}`);
    }

    console.log("\n--- Authentication API Proxy ---");
    const apiService = new ApiService();
    const secureProxy = new AuthProxy(apiService, "SECRET_JWT_TOKEN_123");
    const response = await secureProxy.sendData({ report: "Daily total: 100 packages" });
    console.log("Proxy API Server Response:", response);

    console.log("\n=== SIMULATION FINISHED SUCCESSFULLY ===");
}

runSimulation();
