document.addEventListener('DOMContentLoaded', () => {
  // Use event delegation for better performance (especially for dynamic content)
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('alert__close')) {
      // Find the closest parent alert and remove it with a fade-out effect
      const alert = e.target.closest('.alert');
      if (alert) {
        alert.style.transition = 'opacity 0.3s ease';
        alert.style.opacity = '0';
        
        // Remove after animation completes
        setTimeout(() => {
          alert.remove();
        }, 300);
      }
    }
  });

  // Optional: Auto-remove alerts after 5 seconds
  const autoRemoveAlerts = () => {
    document.querySelectorAll('.alert').forEach(alert => {
      setTimeout(() => {
        alert.style.transition = 'opacity 0.3s ease';
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 300);
      }, 5000);
    });
  };
  autoRemoveAlerts();
});