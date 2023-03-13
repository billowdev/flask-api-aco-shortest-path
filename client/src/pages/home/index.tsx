import React from 'react'
import logo from '../../assets/images/logo/snru.png';
import '../../styles/App.css';

type Props = {}

function HomePage({}: Props) {
  return (

	<div className="App">
	<div> <header className="App-header">
	<img src={logo} className="App-logo" alt="logo" />
	<p>
	  ระบบนำทางภายในมหาวิทยาลัย
	</p>
	<a
	  className="App-link"
	  href="/navigation"
	  rel="noopener noreferrer"
	>
	  เริ่มต้นใช้งาน
	</a>
  </header></div>
  </div>
  )
}

export default HomePage