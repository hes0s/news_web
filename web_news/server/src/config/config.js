module.exports =  {
    port: process.env.P8081,

    db: {
        database: process.env.DB_NAME || 'news',
        user: process.env.DB_USER || 'root',
        password: process.env.DB_PASS || 'root',
        options: {
            dialect: process.env.DIALECT || 'sqlite',
            host: process.env.HOST || 'localhost',
            storage: './web_news.sqlite'
        }
    }
}