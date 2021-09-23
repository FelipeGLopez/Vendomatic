import { useState, useEffect } from "react";
import React from "react";
import BeverageList from "../components/Beverage/BeverageList";

const MachineStorePage = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [beverageList, setBeverageList] = useState([]);

  useEffect(() => {
    setIsLoading(true);

    const data = fetch("http://localhost:8000/inventory/")
      .then((response) => response.json())
      .then((data) => console.log(data));

    setBeverageList(data);
    setIsLoading(false);
  }, []);

  return !isLoading && <BeverageList items={beverageList} />;
};

export default MachineStorePage;
