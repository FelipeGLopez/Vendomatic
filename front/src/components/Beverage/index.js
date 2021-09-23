import React from "react";
import axios from "axios";

const BeverageList = (props) => {
  const { items, setCoins } = props;

  const buyItem = (id) => {
    axios
      .put(`http://localhost:8000/inventory/${id}/`)
      .then((response) => response.headers)
      .then(
        (data) => {
          setCoins(data["x-coins"]);
        },
        (error) => console.log(error)
      );
  };

  return (
    items.length >= 0 && (
      <>
        {items.map((item) => {
          return (
            <div key={item.id}>
              <div>Beverage: {item.name}</div>
              <div>$ {item.value}</div>
              <div>Remaining: {item.quantity}</div>
              <div>
                <button onClick={() => buyItem(item.id)}>
                  Buy {item.name}
                </button>
              </div>
            </div>
          );
        })}
      </>
    )
  );
};

export default BeverageList;
