import React from "react";
import { axiosInstance } from "../../utils/axiosInstance";

const BeverageList = (props) => {
  const { items, setCoins, setText } = props;

  const buyItem = (id, name) => {
    axiosInstance
      .put(`/inventory/${id}/`)
      // .then((response) => response)
      .then(
        (response) => {
          setCoins(response.headers["x-coins"]);
          setText(`You bought ${response.data.quantity} ${name}!`);
        },
        (error) => {
          if (error.response.status === 404) {
            setText(
              `You have ${error.response.headers["x-coins"]} coins!\nThere are no ${name} beverages left!`
            );
          } else if (error.response.status === 400) {
            setText(`You have ${error.response.headers["x-coins"]} coins!`);
          } else {
            console.log(error);
          }
        }
      );
  };

  return (
    items.length >= 0 && (
      <div className="row">
        {items.map((item) => {
          return (
            <div key={item.id}>
              <div className="col-sm-6">
                <div className="card" style={{ margin: "2%" }}>
                  <div className="card-body">
                    <h5 className="card-title">Beverage: {item.name}</h5>
                    <div className="card-text">$ {item.value}</div>
                    <div
                      style={{ color: item.quantity === 0 ? "red" : null }}
                      className="card-text"
                    >
                      Remaining: {item.quantity}
                    </div>
                    <div>
                      <button
                        className="btn btn-primary"
                        onClick={() => buyItem(item.id, item.name)}
                      >
                        Buy {item.name}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    )
  );
};

export default BeverageList;
