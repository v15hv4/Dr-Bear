/**
 * View component for displaying the sentiment score of a response item
 */

const Sentiment = ({ sentiment, className }) => {
    switch (sentiment) {
        case -1:
            return (
                <div className={`text-danger h5 mt-1 ${className}`}>
                    <b>NEGATIVE</b>
                </div>
            );
        case 1:
            return (
                <div className={`text-success h5 mt-1 ${className}`}>
                    <b>POSITIVE</b>
                </div>
            );
        default:
            return (
                <div className={`text-warning h5 mt-1 ${className}`}>
                    <b>NEUTRAL</b>
                </div>
            );
    }
};

export default Sentiment;
