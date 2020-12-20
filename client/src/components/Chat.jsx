import { useState, useRef } from "react";
import { Container, Input, Button, Form } from "reactstrap";

import InMessage from "./InMessage";
import OutMessage from "./OutMessage";

import RedditSample from "./reddit_sampledata.json";
import NewsSample from "./news_sampledata.json";

const Chat = ({ setContent, setLoading }) => {
    const messageInput = useRef(null);

    const [typing, setTyping] = useState(false);
    const [input, setInput] = useState("");
    // const [predictions, setPredictions] = useState([]);
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
            setLoading(true);
        }, 500);

        const newHistory = [{ id: messages.length + 1, type: "out", content: input }, ...messages];
        setMessages(newHistory);

        // send input to server; update message list and setContent from response
        setTimeout(async () => {
            // TODO: new API calls

            // const res = await axios.post(
            //     "/chat/",
            //     { input: input },
            //     { headers: { "Content-Type": "application/json" } }
            // );
            // console.log(res);

            // if (res.data.message !== "") {
            //     setMessages([
            //         ...newHistory,
            //         { id: newHistory.length + 1, type: "in", content: res.data.message },
            //     ]);
            // }
            // setPredictions(res.data.predictions);
            // setContent(res.data.objs);

            // TODO: un-hardcode and set both source and data from API response
            if (input.split(" ").includes("reddit")) {
                setContent({
                    source: "reddit",
                    data: RedditSample,
                });
            } else if (input.split(" ").includes("twitter")) {
                setContent({
                    source: "twitter",
                    data: "",
                });
            } else if (input.split(" ").includes("news")) {
                setContent({
                    source: "news",
                    data: NewsSample,
                });
            }

            setTyping(false);
            setLoading(false);
        }, 1000);

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
                {/* {predictions.length ? ( */}
                {/*     <div className="mt-2"> */}
                {/*         <div className="m-1"> Related keywords: </div> */}
                {/*         {predictions.map((p) => ( */}
                {/*             <Badge color="dark" className="m-1 p-2"> */}
                {/*                 {p} */}
                {/*             </Badge> */}
                {/*         ))} */}
                {/*     </div> */}
                {/* ) : null} */}
            </Container>
        </Container>
    );
};

export default Chat;
