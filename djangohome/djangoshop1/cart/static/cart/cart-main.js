window.onload = () => {
    const clearCartBtn = document.getElementById('clear');

    clearCartBtn.onclick = (e) => {
        clearCart().then(d => d.json()).then(() => {
            setTimeout(() => {
                location.reload();
                console.log('wow');
            }, 500)
        });
        e.preventDefault();
    };

    function clearCart() {
        fetch('/cart/clear', {method: 'DELETE'})
    }


    document.querySelector('.products-wrapper').addEventListener('click', (e) => {
            const target = e.target;
            const checkClassTarget = className => target.classList.contains(className);
            const fetchProductID = function (url, method = 'PUT') {
                console.log(url);
                fetch(url, {method, body: JSON.stringify({product_id: getProductID(target)})}).then(() => {
                    location.reload()
                })
            };
            if (checkClassTarget('plus')) {
                fetchProductID('/cart/add', method = 'POST')
            }
            else if (checkClassTarget('minus')) {
                fetchProductID('/cart/minus-products')
            }
            else if (checkClassTarget('delete')) {
                fetchProductID('/cart/clear-position');
            }
        }
    );

    function getProductID(button) {
        return button.closest('.product').dataset.id
    }

};