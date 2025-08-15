document.getElementById('email').addEventListener('click', function() {
    this.select();
    document.execCommand('copy');
    alert('done copy');
});