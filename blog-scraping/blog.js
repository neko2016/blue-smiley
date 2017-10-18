const request = require("request");
const cheerio = require("cheerio");
const fs = require("fs");

let count = 1;
let timer = setInterval(function(){
    let base = "https://blog.intercom.com/page/";
    // let base = "https://blog.intercom.com/category/product-management/page/";
    let url = base + count;
    console.log(url);
    crawl(url);
    count++;
    if(count === 72) {
        clearInterval(timer);
    }
}, 1000);

function crawl(uri){
    request(uri, (function(uri){
        return function (err, res, data){
            if(err){
                console.log("error occured when requesting uri", uri, err); 
                return err;
            }
            if (res.statusCode === 200){
                let $ = cheerio.load(data);
                 $("h3.post__title > a").each(function(){
                    let title = $(this).text();
                    let link = $(this).attr("href");
                    fs.appendFileSync("all_blogs.txt", title + " - " + link + "\n"); 
                    // fs.appendFile("all_blogs.txt", title + " - " + link + "\n");
                 });
            }
        }
    })(uri));
}