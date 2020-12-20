import { Container } from "reactstrap";
import { Spinner } from "reactstrap";
import FadeIn from "react-fade-in";

/**
 * Intermediate loading screen
 */

const Loading = () => {
    return (
        <Container
            fluid
            tag={FadeIn}
            className="d-flex flex-column justify-content-center align-items-center greeting-container"
        >
            <Spinner color="light" style={{ width: "5rem", height: "5rem" }} />
        </Container>
    );
};

export default Loading;
