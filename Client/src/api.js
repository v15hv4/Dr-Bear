import axios from "axios";

// Common request headers to communicate with the API
const headers = { "Content-Type": "application/json" };

// Method to send input text to the API and fetch a response
export const handleMessage = async (input) => {
    try {
        return await axios.post("/chat/", { input: input }, { headers: headers });
    } catch (err) {
        return err.response;
    }
};
