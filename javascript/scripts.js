document.addEventListener('DOMContentLoaded', () => {
    const apiKey = 'f994c637eea34cc8b11c93c7f66ec582'; 
    const baseApiEndpoint = 'https://newsapi.org/v2/everything?q=expenses&apiKey=' + apiKey;

    function getApiEndpoint() {
        const timestamp = new Date().getTime();
        return `${baseApiEndpoint}&_=${timestamp}`;
    }

    async function fetchArticles() {
        try {
            const response = await fetch(getApiEndpoint());
            const data = await response.json();

            displayArticles(data.articles);
        } catch (error) {
            console.error('Error fetching the articles:', error);
        }
    }

    function displayArticles(articles) {
        const articlesContainer = document.getElementById('articles');
        articlesContainer.innerHTML = ''; 

        articles.forEach(article => {
            const articleElement = document.createElement('div');
            articleElement.classList.add('article');

            articleElement.innerHTML = `
                <h2>${article.title}</h2>
                <p>${article.description}</p>
                <a href="${article.url}" target="_blank">Read more</a>
            `;

            articlesContainer.appendChild(articleElement);
        });
    }

    fetchArticles();
});