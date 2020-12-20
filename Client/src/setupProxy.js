const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (app) {
    app.use(
        "/chat",
        createProxyMiddleware({
            target: "http://52.151.193.38",
            changeOrigin: true,
        })
    );
};
