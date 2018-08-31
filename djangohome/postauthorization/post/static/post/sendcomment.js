window.onload = () => {
    window.addEventListener('submit', e => {
        e.preventDefault();
        const target = e.target;
        if (target.classList.contains('form-comment')) {
            const textComment = target.getElementsByClassName('text-new-comment')[0].value;
            target.getElementsByClassName('text-new-comment')[0].value = '';
            const idPost = target.closest('.post').dataset.id;
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
                addCommentToPost(userName, textComment, target.closest('.post').querySelector('.comments'))
            });
        }
    })
};

function addCommentToPost(userName, commentText, postElement) {
    const comentElement = document.createElement('div');
    comentElement.innerHTML = `<h3> ${userName} :</h3>
                                ${commentText}`;
    postElement.appendChild(comentElement);
}
