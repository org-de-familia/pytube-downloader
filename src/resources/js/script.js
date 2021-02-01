var video_download_url = '/video/download'
var audio_download_url = '/audio/download'

function download_video(url){
    download_file(url, video_download_url)
}

function download_audio(url){
    download_file(url, audio_download_url)
}

function download_file(url_element_id, complement){
    url_element = document.getElementById(url_element_id);

    if (validate_url(url_element.value))
    {
        url = complement + '?url=' + url_element.value;
        download(url);
    } else {
        alert('Insira uma URL válida.');
    }
}

function download(url){
    let element = document.createElement('a')
    element.setAttribute('href', url);
    element.style.visibility = 'hidden';

    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element)
}

function validate_url(url){
    if(url == '')
        return false;
    if(url.search('http://') != 0 && url.search('https://') != 0)
        return false;

    return true;
}