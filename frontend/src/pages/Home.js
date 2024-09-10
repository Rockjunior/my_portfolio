import React from 'react';
import AboutMe from '../components/AboutMe';
import AcademicJourney from '../components/AcademicJourney';
import SWEJourney from '../components/SWEJourney';

const Home = () => {
  return (
    <div>
      <h1>Welcome to My Portfolio</h1>
      <AboutMe />
      <AcademicJourney />
      <SWEJourney />
    </div>
  );
};

export default Home;