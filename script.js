const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function registerUser(event) {
    event.preventDefault(); // Ngăn chặn form gửi đi

    // Lấy thông tin từ form
    const name = document.getElementById('sign-up-name').value;
    const email = document.getElementById('sign-up-email').value;
    const password = document.getElementById('sign-up-password').value;

    // Kiểm tra xem người dùng đã đăng ký chưa
    const existingUser = JSON.parse(localStorage.getItem('users')) || [];
    const userExists = existingUser.find(user => user.email === email);

    if (userExists) {
        alert('Email already registered. Please sign in.');
    } else {
        // Lưu thông tin người dùng vào localStorage
        existingUser.push({ name, email, password });
        localStorage.setItem('users', JSON.stringify(existingUser));
        alert('Registration successful! You can now sign in.');
    }
}

function loginUser(event) {
    event.preventDefault(); // Ngăn chặn form gửi đi

    // Lấy thông tin từ form
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    // Kiểm tra thông tin đăng nhập
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const user = users.find(user => user.email === email && user.password === password);

    if (user) {
        alert(`Welcome back, ${user.name}!`);
        // Chuyển hướng tới trang trò chơi hoặc trang chính
        window.location.href = 'game.html'; // Thay đổi đường dẫn theo trang chính của bạn
    } else {
        alert('Invalid email or password. Please try again.');
    }
}