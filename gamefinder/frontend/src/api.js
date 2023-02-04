export default {
    getConfig: () => fetch('/api/setup/').then(resp => resp.json())
}
