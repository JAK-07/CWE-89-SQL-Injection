┌──(kali㉿Kali)-[~]
└─$ docker logs juice-shop.pc --tail 50
info: All dependencies in ./package.json are satisfied (OK)
info: Detected Node.js version v12.16.2 (OK)
info: Detected OS linux (OK)
info: Detected CPU x64 (OK)
info: Required file index.html is present (OK)
info: Required file styles.css is present (OK)
info: Required file main-es2015.js is present (OK)
info: Required file tutorial-es2015.js is present (OK)
info: Required file polyfills-es2015.js is present (OK)
info: Required file runtime-es2015.js is present (OK)
info: Required file vendor-es2015.js is present (OK)
info: Required file main-es5.js is present (OK)
info: Required file tutorial-es5.js is present (OK)
info: Required file polyfills-es5.js is present (OK)
info: Required file runtime-es5.js is present (OK)
info: Required file vendor-es5.js is present (OK)
info: Configuration default validated (OK)
info: Port 3000 is available (OK)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Wallets
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Feedbacks
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Complaints
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Users
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Users
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
Unhandled rejection SequelizeDatabaseError: SQLITE_ERROR: no such table: Users
    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)
    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)
    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)
    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:16:21)
info: Server listening on port 3000
info: Solved challenge Login Admin (Log in with the administrator's user account.)

┌──(kali㉿Kali)-[~]
└─$ 
