export class BiDirectionalPriorityQueue {
    constructor() {
        this.elements = [];
    }

    enqueue(item, priority) {
        this.elements.push({ item, priority, insertedAt: Date.now() });
    }

    _sorted(highest, oldest) {
        return [...this.elements].sort((a, b) => {
            if (a.priority !== b.priority) {
                return highest ? b.priority - a.priority : a.priority - b.priority;
            }
            return oldest ? a.insertedAt - b.insertedAt : b.insertedAt - a.insertedAt;
        });
    }

    dequeue(highest = true, oldest = true) {
        if (this.elements.length === 0) return null;
        const sorted = this._sorted(highest, oldest);
        const top = sorted[0];
        this.elements = this.elements.filter(e => e !== top);
        return top.item;
    }

    peek(highest = true, oldest = true) {
        if (this.elements.length === 0) return null;
        return this._sorted(highest, oldest)[0].item;
    }
}
