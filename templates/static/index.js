console.log('Ez csak egy gyakorló szöveg')

const refuelsEl = document.querySelector('#refuels')
fetch('/api/refuels/')
.then(res => res.json())
.then(data => {
        data.forEach(refuel => {
            element = document.createElement('div')
            element.innerText = refuel.distance_km
            refuelsEl.appendChild(element)
            
        });
})