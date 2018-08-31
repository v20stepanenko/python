const getPosts = function () {
    fetch('/post/all').then(data => data.json()).then(data => {
        const generator = generatePosts('.post-wrapper');
        data.forEach(item => {
            generator(item)
        })
    })
};


const generatePosts = function (wrapperSelector) {
    let wrapperPost = document.querySelector(wrapperSelector);
    return function (post) {
        console.log(post);
        const postBlock = document.createElement('div');
        postBlock.id = `post${post.post_id}`;
        postBlock.classList.add('post');
        const title = document.createElement('a');
        title.href = `/post/${post.post_id}`;
        title.innerText = post.post_title;
        const article = document.createElement('article');
        article.innerText = post.post_body;
        postBlock.appendChild(title);
        postBlock.appendChild(article);
        wrapperPost.appendChild(postBlock);
        console.log(wrapperPost);
    };
};
window.onload = () => {
    getPosts();
};