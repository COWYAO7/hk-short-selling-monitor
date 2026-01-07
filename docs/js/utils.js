/**
 * 通用工具函数
 */

// 格式化日期
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
    });
}

// 格式化时间
function formatDateTime(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// 格式化数字（添加千位分隔符）
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// 加载JSON数据
async function loadJSON(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('加载数据失败:', error);
        throw error;
    }
}

// 显示加载状态
function showLoading(containerId) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>正在加载数据...</p>
            </div>
        `;
    }
}

// 显示错误信息
function showError(containerId, message) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">⚠️</div>
                <p>${message}</p>
            </div>
        `;
    }
}

// 显示空状态
function showEmpty(containerId, message) {
    const container = document.getElementById(containerId);
    if (container) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">📭</div>
                <p>${message}</p>
            </div>
        `;
    }
}

// 高亮当前导航
function highlightCurrentNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// 表格排序
function sortTable(table, column, ascending = true) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    rows.sort((a, b) => {
        const aValue = a.children[column].textContent.trim();
        const bValue = b.children[column].textContent.trim();

        // 尝试转换为数字
        const aNum = parseFloat(aValue);
        const bNum = parseFloat(bValue);

        if (!isNaN(aNum) && !isNaN(bNum)) {
            return ascending ? aNum - bNum : bNum - aNum;
        }

        // 字符串比较
        return ascending
            ? aValue.localeCompare(bValue, 'zh-CN')
            : bValue.localeCompare(aValue, 'zh-CN');
    });

    // 重新插入排序后的行
    rows.forEach(row => tbody.appendChild(row));
}

// 搜索过滤
function filterTable(table, searchText) {
    const tbody = table.querySelector('tbody');
    const rows = tbody.querySelectorAll('tr');

    const lowerSearchText = searchText.toLowerCase();

    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        if (text.includes(lowerSearchText)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// 防抖函数
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Toast 通知
function showToast(message, type = 'info') {
    // 创建toast容器（如果不存在）
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
        `;
        document.body.appendChild(toastContainer);
    }

    // 创建toast元素
    const toast = document.createElement('div');
    toast.style.cssText = `
        background: rgba(30, 41, 59, 0.95);
        backdrop-filter: blur(20px);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
        border-left: 4px solid ${type === 'success' ? '#00ff88' : type === 'error' ? '#ff6b6b' : '#3b82f6'};
        animation: slideIn 0.3s ease;
    `;
    toast.textContent = message;

    // 添加动画
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
    `;
    document.head.appendChild(style);

    toastContainer.appendChild(toast);

    // 3秒后自动移除
    setTimeout(() => {
        toast.style.animation = 'slideIn 0.3s ease reverse';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// 导出CSV
function exportTableToCSV(table, filename) {
    const rows = table.querySelectorAll('tr');
    const csv = [];

    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const rowData = Array.from(cols).map(col => {
            let text = col.textContent.trim();
            // 转义双引号并用双引号包裹
            text = text.replace(/"/g, '""');
            return `"${text}"`;
        });
        csv.push(rowData.join(','));
    });

    // 创建下载链接
    const csvContent = '\uFEFF' + csv.join('\n'); // 添加BOM以支持中文
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.click();

    showToast('导出成功！', 'success');
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    highlightCurrentNav();
});
