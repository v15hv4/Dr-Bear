import { Container } from "reactstrap";

import FadeIn from "react-fade-in";

const RedditItem = ({ comment }) => {
    return <div className="h5 my-3">"{comment}"</div>;
};

const Reddit = ({ data }) => {
    return (
        <Container tag={FadeIn} className="text-light">
            <div className="display-4 d-flex align-items-center">
                Here's what people say on
                <img src="./Reddit-Logo.wine.svg" alt="reddit" className="reddit-logo ml-n3" />
                <span className="ml-n4">...</span>
            </div>
            <div>
                {Object.keys(data).map((subreddit, idx) => (
                    <div className="mb-5" key={idx}>
                        <div className="h3 mb-4">
                            <b>r/{subreddit}</b>
                        </div>
                        {data[subreddit].map((comment, cidx) => (
                            <RedditItem comment={comment} key={cidx} />
                        ))}
                    </div>
                ))}
            </div>
        </Container>
    );
};

export default Reddit;
