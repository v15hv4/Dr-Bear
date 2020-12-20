import { useState, useRef } from "react";
import { Container, Input, Button, Form } from "reactstrap";
import { handleMessage } from "../api.js";

import InMessage from "./InMessage";
import OutMessage from "./OutMessage";

import RedditSample from "./reddit_sampledata.json";
import TwitterSample from "./twitter_sampledata.json";
import NewsSample from "./news_sampledata.json";

const Chat = ({ setContent, setLoading }) => {
    const messageInput = useRef(null);

    const [typing, setTyping] = useState(false);
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([
        {
            id: 0,
            type: "in",
            content: "Hello there! How may I help you today?",
        },
    ]);

    const sendMessage = (e) => {
        e.preventDefault();
        if (input === "") return;

        setTimeout(() => {
            setTyping(true);
        }, 500);

        const newHistory = [{ id: messages.length + 1, type: "out", content: input }, ...messages];
        setMessages(newHistory);

        // send input to server; update message list and setContent from response
        setTimeout(async () => {
            if (input === "") return;

            const res = await handleMessage(input);

            if (res.data.message !== "") {
                setMessages([
                    { id: newHistory.length + 1, type: "in", content: res.data.message },
                    ...newHistory,
                ]);
            }

            if (res.data.data) {
                setLoading(true);
            }

            if (res.data.source !== "") {
                console.log(res.data);
                setContent(res.data);
                // setContent({
                //     ...res.data,
                //     data:
                //         res.data.source === "twitter"
                //             ? TwitterSample
                //             : res.data.source === "reddit"
                //             ? RedditSample
                //             : res.data.source === "news"
                //             ? NewsSample
                //             : null,
                // });
            }

            setTyping(false);
            setLoading(false);
        }, 500);

        setInput("");
        messageInput.current.focus();
    };
    return (
        <Container fluid className="d-flex flex-column chatbar justify-content-between py-3">
            <Container fluid className="overflow-auto mb-4 message-container">
                {typing ? <InMessage typing /> : null}
                {messages.map((message) =>
                    message.type === "in" ? (
                        <InMessage key={message.id} {...message} />
                    ) : (
                        <OutMessage key={message.id} {...message} />
                    )
                )}
            </Container>
            <Container fluid className="px-0">
                <Form className="d-flex flex-row" onSubmit={sendMessage}>
                    <Input
                        autoFocus
                        type="text"
                        value={input}
                        placeholder="Type a message..."
                        onChange={(e) => (typing ? null : setInput(e.target.value))}
                        innerRef={messageInput}
                        className="message-input"
                    />
                    <Button
                        color="dark"
                        className="ml-2 d-flex flex-column justify-content-center send-btn"
                    >
                        <img src="/send-white-18dp.svg" alt="Send" />
                    </Button>
                </Form>
            </Container>
        </Container>
    );
};

export default Chat;
