import { Container } from "reactstrap";

import FadeIn from "react-fade-in";

const NewsItem = ({ news }) => {
    return (
        <div className="h2 my-5">
            <b>
                <a target="_blank" rel="noreferrer" href={news.url}>
                    {news.title.split("-").slice(0, -1).join(" ")}
                </a>
            </b>
            <footer className="mt-2 text-muted h4">{news.title.split("-").slice(-1)[0]}</footer>
        </div>
    );
};

const News = ({ data }) => {
    return (
        <Container tag={FadeIn} className="text-light">
            <div className="display-4 d-flex align-items-center mt-5 pt-2 pb-3">In the news...</div>
            <div className="mt-5">
                {data.map((news, idx) => (
                    <NewsItem news={news} key={idx} />
                ))}
            </div>
        </Container>
    );
};

export default News;
