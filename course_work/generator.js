export function* packageGenerator() {
    const types = ["Standard", "Express", "VIP", "Fragile"];
    let id = 1;
    while (true) {
        const type = types[Math.floor(Math.random() * types.length)];
        const weight = parseFloat((Math.random() * 50 + 0.5).toFixed(2));
        yield { id: id++, type, weight, timestamp: Date.now() };
    }
}

export async function consumeGeneratorWithTimeout(generator, durationInSeconds, callback) {
    const iterator = generator();
    const endTime = Date.now() + durationInSeconds * 1000;
    while (Date.now() < endTime) {
        const { value } = iterator.next();
        callback(value);
        await new Promise(resolve => setTimeout(resolve, 200));
    }
}
