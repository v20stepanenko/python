window.onload = () => {
    const startComment = () => {
        fetch('http://localhost/post/1/comments/').then(d => d.json()).then(d => {
            console.log(d[0]);
            d.forEach(item => {
                generateComment(item)
            })
        });
    };

    const commentsWrapper = document.getElementsByClassName('comments-wrapper')[0];

    const generateComment = function (comment) {
        const commentBlock = document.createElement('div');
        commentBlock.classList.add('comment-block');
        const author = document.createElement('a');
        author.innerText = comment.author.name;

        author.href = `user/${comment.author.id}`;
        commentBlock.appendChild(author);
        const commentBody = document.createElement('div');
        commentBody.classList.add('comment-text');
        commentBody.innerText = comment.body;
        commentBlock.appendChild(commentBody);
        if (comment.can_del) {
            const btnDelComment = document.createElement('a');
            btnDelComment.href = `comment/del/${comment.comment_id}`;
            btnDelComment.innerText = 'Удалить';
            commentBlock.appendChild(btnDelComment);
            btnDelComment.addEventListener('click', e => {
                e.preventDefault();
                const btn = this;
                fetch(btnDelComment.href).then(d => {
                    btn.remove();
                })
            })
        }

        commentsWrapper.appendChild(commentBlock);
    };

    startComment();

    window.addEventListener('submit', e => {
        e.preventDefault();
        const target = e.target;
        const textArea = target.querySelector('textarea');
        const textComment = textArea.value;
        if (target.classList.contains('comments-add')) {
            const idPost = document.querySelector('.post_block').dataset.id;
            fetch(target.action, {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    body: textComment,
                    post_id: idPost
                })
            }).then(d => {
                const comment = {
                    body: textArea.value,
                    can_del: true,
                    author: {
                        id: user.id,
                        name: user.name
                    }
                };
                textArea.value = '';
                generateComment(comment)
            });
        }
    })
};