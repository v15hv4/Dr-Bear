import { Card, CardBody, Row } from "reactstrap";
import FadeIn from "react-fade-in";
import ReactLoading from "react-loading";

const InMessage = ({ content, typing }) => {
    return (
        <FadeIn delay="10" childTag={Row} className="d-flex justify-content-start my-2">
            <Card className="in-message">
                <CardBody className="py-2 px-3">
                    {typing ? <ReactLoading type="bubbles" width="30px" height="30px" /> : content}
                </CardBody>
            </Card>
        </FadeIn>
    );
};

export default InMessage;
