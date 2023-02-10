const defaultHeaders = {
    'Content-Type': 'application/json',
};

export const api = {
    getConfig: () => fetch('/api/setup/').then(resp => resp.json()),
    setConfig: (username, password) => {
        return fetch('/api/setup/', {
            method: 'POST',
            headers: defaultHeaders,
            body: JSON.stringify({username, password})
        }).then(resp => resp.json())
        .then(json => {
            return json;
        });
    },
    login: (username, password) => {
        return fetch('/api/auth/', {
            method: 'POST',
            headers: defaultHeaders,
            body: JSON.stringify({username, password})
        }).then(resp => resp.json());
    },
    getCurrentUser: () => fetch('/api/auth/').then(resp => resp.json()),
    logout: () => {
        return fetch('/api/auth/', {
            method: 'DELETE',
            headers: defaultHeaders,
        }).then(resp => resp.json());
    },
    bggSearch: query => fetch(`/api/admin/search/?query=${query}`).then(resp => resp.json()),
    addGame: (gameId, shelfId, row, column) => fetch('/api/admin/games/', {
        method: 'POST',
        headers: defaultHeaders,
        body: JSON.stringify({game_id: gameId, shelf_id: shelfId, row, column})
    }).then(resp => resp.json()),
    addShelf: (name, type, width, height) => fetch('/api/admin/shelves/', {
        method: 'POST',
        headers: defaultHeaders,
        body: JSON.stringify({name, type, width, height})
    }).then(resp => resp.json()),
    getShelves: () => fetch('/api/admin/shelves/').then(resp => resp.json()),
    getGame: id => fetch(`/api/games/${id}`).then(resp => resp.json()),
    getGames: (page=1) => fetch(`/api/games/?page=${page}&per_page=8`).then(resp => resp.json()),
}

export default api;
