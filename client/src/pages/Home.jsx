import { useState } from "react";
import { Container, Row, Col } from "reactstrap";
import FadeIn from "react-fade-in";

import Chat from "../components/Chat";
import Loading from "../components/Loading";
import Greeting from "../components/Greeting";
import Reddit from "../components/Reddit";

const Home = () => {
    const [loading, setLoading] = useState(false);
    const [content, setContent] = useState([]);

    const renderContent = () => {
        if (loading) {
            return <Loading />;
        } else {
            switch (content.source) {
                case "reddit":
                    return <Reddit {...content} />;
                // case "twitter":
                //     return <Twitter {...content} />;
                // case "news":
                //     return <News {...content} />;
                default:
                    return <Greeting />;
            }
        }
    };

    return (
        <Container fluid>
            <Row className="mx-3">
                <Col>
                    <Container fluid className="overflow-auto" style={{ maxHeight: "90vh" }}>
                        {renderContent()}
                    </Container>
                </Col>
                <Col md={4} style={{ borderLeft: "1px solid #333" }}>
                    <Chat setContent={setContent} setLoading={setLoading} />
                </Col>
            </Row>
        </Container>
    );
};

export default Home;
