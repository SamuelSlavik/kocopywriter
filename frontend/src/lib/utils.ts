


export const scrollToTarget = function(targetId: string, offset = 0) {
  const targetElement = document.getElementById(targetId);

  if (targetElement) {
    const targetPosition = targetElement.offsetTop - offset;

    window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
    });
  }
};

export const formatDate = (date: string) => {
  const [year, month, day] = date.split('-');
  return `${day}.${month}.${year}`;
}