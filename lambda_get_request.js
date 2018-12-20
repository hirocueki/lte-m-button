const https = require('https');

const setStatus={
    "SINGLE": "single",
    "DOUBLE": "double",
    "LONG": "long"
}

exports.handler = async (event, context) => {

    return new Promise((resolve, reject) => {
        var query = setStatus[event.deviceEvent.buttonClicked.clickType]
        const options = {
            host: 'example.com',
            path: '/foo/bar/buzz.php?query=' + query,
            //port: 80,
            method: 'GET'
        };

        const req = https.request(options, (res) => {
          resolve('Success');
        });

        req.on('error', (e) => {
          reject(e.message);
        });

        // send the request
        req.write('');
        req.end();
    });
};
