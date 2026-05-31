export function withLogging(level, fn) {
    return function (...args) {
        const timestamp = new Date().toISOString();
        if (level === "ERROR") {
            try {
                return fn(...args);
            } catch (error) {
                console.log(`[${timestamp}] [ERROR] Arguments: ${JSON.stringify(args)} | Error: ${error.message}`);
                throw error;
            }
        }
        console.log(`[${timestamp}] [${level}] Called with: ${JSON.stringify(args)}`);
        const result = fn(...args);
        console.log(`[${timestamp}] [${level}] Returned: ${JSON.stringify(result)}`);
        return result;
    };
}
