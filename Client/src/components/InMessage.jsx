import { Card, CardBody, Row } from "reactstrap";
import FadeIn from "react-fade-in";

const InMessage = ({ content, typing }) => {
    return (
        <FadeIn delay="10" childTag={Row} className="d-flex justify-content-start my-1">
            <Card className="in-message">
                <CardBody className="py-2 px-3">{typing ? "Typing..." : content}</CardBody>
            </Card>
        </FadeIn>
    );
};

export default InMessage;