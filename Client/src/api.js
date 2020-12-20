import axios from "axios";

const headers = { "Content-Type": "application/json" };

export const handleMessage = async (input) => {
    try {
        return await axios.post("/chat/", { input: input }, { headers: headers });
    } catch (err) {
        return err.response;
    }
};
