import { Container } from "reactstrap";
import { Tweet } from "react-twitter-widgets";

import FadeIn from "react-fade-in";
import Masonry from "react-masonry-css";

const TwitterItem = ({ tweet }) => {
    return <Tweet tweetId={tweet} options={{ theme: "dark" }} />;
};

const Twitter = ({ data }) => {
    return (
        <Container tag={FadeIn} className="text-light">
            <div className="display-4 d-flex align-items-center mt-5 pt-2 pb-3">
                Trending on
                <img src="./twitter-seeklogo.com.svg" alt="larry" className="twitter-logo ml-3" />
                <img src="./Twitter_text.svg" alt="twitter" className="twitter-text ml-2" />
                <span className="ml-n2">...</span>
            </div>
            <div className="mt-5">
                <Masonry
                    breakpointCols={{ default: 2 }}
                    className="tweet-grid"
                    columnClassName="tweet-grid-column"
                >
                    {data.map((tweet, idx) => (
                        <TwitterItem tweet={tweet} key={idx} />
                    ))}
                </Masonry>
            </div>
        </Container>
    );
};

export default Twitter;
