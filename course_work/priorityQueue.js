export class PriorityQueue {
    constructor() {
        this.elements = [];
    }

    enqueue(item, priority) {
        this.elements.push({item, priority, insertedAt: Date.now()});
    }

    sorted(highest, oldest) {
        return [...this.elements].sort((a, b) => {
            if (a.priority !== b.priority) {
                return highest ? b.priority - a.priority : a.priority - b.priority;
            }
            return oldest ? b.insertedAt - a.insertedAt : a.insertedAt - b.insertedAt ;
        });
    }

    dequeue(highest = true, oldest = true) {
        if (this.elements.length === 0) return;
        const sorted = this.sorted(highest, oldest);
        const top = sorted[0];
        this.elements = this.elements.filter(e => e !== top);
        return top.item;
    }
}