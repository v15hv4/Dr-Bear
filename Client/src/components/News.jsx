import { Container } from "reactstrap";

import FadeIn from "react-fade-in";
import Sentiment from "./Sentiment";

/**
 * View component for each news item
 */

const NewsItem = ({ title, sentiment, url }) => {
    return (
        <div className="h2 my-5">
            <span
                className={`text-${
                    sentiment === 1 ? "success" : sentiment === -1 ? "danger" : "warning"
                }`}
            >
                {title}
            </span>
            <div className="d-flex align-items-center">
                <Sentiment sentiment={sentiment} />
                <a target="_blank" rel="noreferrer" href={url} className="h5 mt-1 ml-2">
                    READ MORE
                </a>
            </div>
        </div>
    );
};

/**
 * Container and iterator to display news items from the API response
 */

const News = ({ data }) => {
    return (
        <Container tag={FadeIn} className="text-light">
            <div className="display-4 d-flex align-items-center mt-5 pt-2 pb-3">In the news...</div>
            <div className="mt-5">
                {data.map((news, idx) => (
                    <NewsItem {...news} key={idx} />
                ))}
            </div>
        </Container>
    );
};

export default News;
