export default function getCSRFToken() {
    let result = null;
    let cookie_key = 'csrftoken';

    if (document.cookie && document.cookie !== '') {
        let cookies = document
            .cookie
            .split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, cookie_key.length + 1) == (cookie_key + '=')) {
                result = decodeURIComponent(cookie.substring(cookie_key.length + 1));
                break;
            }
        }
    }
    return result;
};
