export class ApiService {
    async sendData(payload, headers = {}) {
        if (!headers["Authorization"]) {
            return { status: 401, message: "Unauthorized" };
        }
        return { status: 200, data: `Processed safely: ${JSON.stringify(payload)}` };
    }
}

export class AuthProxy {
    constructor(realService, token) {
        this.realService = realService;
        this.token = token;
    }

    async sendData(payload, headers = {}) {
        const secureHeaders = { ...headers, "Authorization": `Bearer ${this.token}` };
        return await this.realService.sendData(payload, secureHeaders);
    }
}
