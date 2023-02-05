const defaultHeaders = {
    'Content-Type': 'application/json',
};

export default {
    getConfig: () => fetch('/api/setup/').then(resp => resp.json()),
    setConfig: (username, password) => {
        return fetch('/api/setup/', {
            method: 'POST',
            headers: defaultHeaders,
            body: JSON.stringify({username, password})
        }).then(resp => resp.json());
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
}
