const Sentiment = ({ sentiment, className }) => {
    switch (sentiment) {
        case -1:
            return <div className={`text-danger h5 ${className}`}> NEGATIVE </div>;
        case 1:
            return <div className={`text-success h5 ${className}`}> POSITIVE </div>;
        default:
            return <div className={`text-muted h5 ${className}`}> NEUTRAL </div>;
    }
};

export default Sentiment;
