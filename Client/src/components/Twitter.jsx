import { Container } from "reactstrap";
import { Tweet } from "react-twitter-widgets";

import FadeIn from "react-fade-in";
import Masonry from "react-masonry-css";
import Sentiment from "./Sentiment";

const TwitterItem = ({ tweet }) => {
    return (
        <div>
            <Tweet tweetId={tweet.id} options={{ theme: "dark" }} />
            <Sentiment sentiment={tweet.sentiment} className="ml-2 mb-4" />
        </div>
    );
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
                    {data.slice(0, 50).map((tweet, idx) => (
                        <TwitterItem tweet={tweet} key={idx} />
                    ))}
                </Masonry>
            </div>
        </Container>
    );
};

export default Twitter;
