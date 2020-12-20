import { Container } from "reactstrap";
import FadeIn from "react-fade-in";

const Greeting = () => {
    return (
        <Container
            fluid
            tag={FadeIn}
            className="d-flex flex-column justify-content-center align-items-center greeting-container"
        >
            <h1 className="display-3 text-light font-weight-bold">
                Dr <span className="text-warning">Bear</span>
            </h1>
            <h3 className="mt-3 text-muted">The Doctor at Wall Street.</h3>
        </Container>
    );
};

export default Greeting;
