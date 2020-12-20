import { Card, CardBody, Row } from "reactstrap";
import FadeIn from "react-fade-in";

const OutMessage = ({ content }) => {
    return (
        <FadeIn delay="10" childTag={Row} className="d-flex justify-content-end my-1">
            <Card className="bg-warning out-message">
                <CardBody className="py-2 px-3">{content}</CardBody>
            </Card>
        </FadeIn>
    );
};

export default OutMessage;
