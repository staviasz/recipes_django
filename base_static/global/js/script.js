(() => {
  const forms = document.querySelectorAll('.form-delete')

  for (const form of forms) {
    form.addEventListener('submit', function (e) {
      e.preventDefault()

      const confirmed = confirm('Are you sure?')

      if (confirmed) {
        form.submit()
      }
    })
  }

  (() => {
    const buttonCloseMenu = document.querySelector('.button-close-menu')
    const buttonShowMenu = document.querySelector('.button-show-menu')
    const menuContainer = document.querySelector('.menu-container')
    const menuHidden = 'menu-hidden'
    const buttonShowMenuVisible = 'button-show-menu-visible'

    const closeMenu = () => {
      buttonShowMenu.classList.add(buttonShowMenuVisible)
      menuContainer.classList.add(menuHidden)
    }
    const ShowMenu = () => {
      buttonShowMenu.classList.remove(buttonShowMenuVisible)
      menuContainer.classList.remove(menuHidden)
    }
    if (buttonCloseMenu) {
      buttonCloseMenu.removeEventListener('click', closeMenu)
      buttonCloseMenu.addEventListener('click', closeMenu)
    }
    if (buttonShowMenu) {
      buttonShowMenu.removeEventListener('click', ShowMenu)
      buttonShowMenu.addEventListener('click', ShowMenu)
    }
  })()
})();

(() => {
  const authorsLogoutLinks = document.querySelectorAll('.authors-logout-link')
  const formLogout = document.querySelector('.form-logout')
  console.log(authorsLogoutLinks)
  for (const link of authorsLogoutLinks) {
    link.addEventListener('click', e => {
      e.preventDefault()
      formLogout.submit()
    })
  }
})()
