'use strict';

window.onload = () => {

    const productsWrapper = document.getElementsByClassName('products-wrapper')[0];
    productsWrapper.addEventListener('click', (event) => {
        const {target} = event;
        if (target.classList.contains('add-product')) {
            event.preventDefault();
            const idGoods = target.dataset.id;
            addGoods(idGoods)
        }
    });

    const setSummaryQuantity = (() => {
        const quantityElem = document.querySelector('#cart .quantity');
        return (summaryQuantity) => {
            quantityElem.innerText = summaryQuantity
        }
    })();

    function addGoods(idGoods) {
        console.log('add product');
        return fetch('/cart/add', {
            method: 'POST',
            body: JSON.stringify({product_id: idGoods})
        }).then(d => d.json()).then(d => {
            const quantity = d['summary_quantity'];
            setSummaryQuantity(quantity)
        })
    }
};