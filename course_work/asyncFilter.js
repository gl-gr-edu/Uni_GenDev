export async function asyncFilter(array, asyncCallback, abortSignal) {
    const results = [];
    for (const item of array) {
        if (abortSignal && abortSignal.aborted) {
            throw new Error("Operation aborted");
        }
        const keep = await asyncCallback(item);
        if (keep) results.push(item);
    }
    return results;
}
