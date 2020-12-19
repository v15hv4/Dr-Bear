import { Card, CardBody, Row } from "reactstrap";
import FadeIn from "react-fade-in";

const OutMessage = ({ content }) => {
    return (
        <Row tag={FadeIn} className="d-flex justify-content-end my-1">
            <Card className="bg-warning out-message">
                <CardBody className="py-2 px-3 ">{content}</CardBody>
            </Card>
        </Row>
    );
};

export default OutMessage;
