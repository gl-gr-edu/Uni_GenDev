export function memoize(fn, config = {}) {
    const cache = new Map();
    const usageOrder = [];
    const maxElements = config.maxSize || Infinity;
    return function (...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            const idx = usageOrder.indexOf(key);
            if (idx > -1) usageOrder.splice(idx, 1);
            usageOrder.push(key);
            return cache.get(key);
        }
        const result = fn(...args);
        if (cache.size >= maxElements) {
            cache.delete(usageOrder.shift());
        }
        cache.set(key, result);
        usageOrder.push(key);
        return result;
    };
}

