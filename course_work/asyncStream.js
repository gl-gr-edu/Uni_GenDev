export function createAsyncStream(dataArray) {
    let index = 0;
    return {
        [Symbol.asyncIterator]() {
            return {
                async next() {
                    if (index < dataArray.length) {
                        const value = dataArray[index++];
                        await new Promise(resolve => setTimeout(resolve, 50));
                        return { value, done: false };
                    }
                    return { done: true };
                }
            };
        }
    };
}
